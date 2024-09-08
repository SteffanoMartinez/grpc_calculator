import grpc
from concurrent import futures
# Import the pb2 (auto_generated protocol services) and grpc (auto_generated server code) all in python.
import calculator_pb2 as calculator_pb2
import calculator_pb2_grpc as calculator_grpc

class CalculatorServicer(calculator_grpc.CalculatorServicer):
    def addition(self, request, context):
        result = request.operand1 + request.operand2
        return calculator_pb2.AdditionResponse(result=result)
    def substraction(self, request, context):
        result = request.operand1 - request.operand2
        return calculator_pb2.SubstractionResponse(result=result)
    def multiplication(self, request, context):
        result = request.operand1 * request.operand2
        return calculator_pb2.MultiplicationResponse(result=result)
    def division(self, request, context):
        if request.dividend == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Division by zero is not allowed.')
            return calculator_pb2.DivisionResponse()
        # Calculate the quotient and remainder
        result = request.divisor / request.dividend  #  Division
        remainder = int(request.divisor) % int(request.dividend)  # Remainder
        return calculator_pb2.DivisionResponse(result=result, remainder=remainder)
    def exponential(self, request, context):
        result = request.base ** request.power
        return calculator_pb2.ExponentialResponse(result=result)

def serve():
    # Create a gRPC server:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

    # Add a port:
    server.add_insecure_port('[::]:50051')
    print("Server started. Listening on port 50051.")

    # Run the server:
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
