import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        a = float(body['a'])
        b = float(body['b'])
        operation = body['operation']
        
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            result = a / b
        else:
            raise ValueError("Invalid operation")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }