import grpc
import calculator_pb2 as calculator_pb2
import calculator_pb2_grpc as calculator_grpc

def run():
    # Create a channel and a stub
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_grpc.CalculatorStub(channel) # Stub hold the auto-generated code for server side API's

        # Create a request
        request_addition = calculator_pb2.AdditionRequest(operand1=10, operand2=20) # Interacting with the proto file message's
        request_substraction = calculator_pb2.SubstractionRequest(operand1=100,operand2=25)
        request_multiplication = calculator_pb2.MultiplicationRequest(operand1=5,operand2=5)
        request_division = calculator_pb2.DivisionRequest(divisor=20.0,dividend=3.0)
        request_exponential = calculator_pb2.ExponentialRequest(base=2,power=8)

        # Make the call
        # Request a service from proto file, sumbitting a request to it.
        # This is the bridge of all things!!!
        response_addition = stub.addition(request_addition) 
        response_substraction = stub.substraction(request_substraction)
        response_multiplication = stub.multiplication(request_multiplication)
        response_division = stub.division(request_division)
        response_exponential = stub.exponential(request_exponential)


        # Print the result
        print(f"Result of addition: {response_addition.result}")
        print(f"Result of substraction: {response_substraction.result}")
        print(f"Result of multiplication: {response_multiplication.result}")
        print(f"Result of division: Result -> {response_division.result} Remainder -> {response_division.remainder}")
        print(f"Result of exponential: {response_exponential.result}")

if __name__ == "__main__":
    run()
