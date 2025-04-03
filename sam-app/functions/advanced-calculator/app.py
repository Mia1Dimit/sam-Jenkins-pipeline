import json
import math

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        operation = body['operation']
        numbers = body.get('numbers', [])
        
        operations = {
            'sqrt': lambda: math.sqrt(numbers[0]),
            'power': lambda: numbers[0] ** numbers[1],
            'log': lambda: math.log(numbers[0], numbers[1]),
            'avg': lambda: sum(numbers)/len(numbers),
            'max': lambda: max(numbers),
            'min': lambda: min(numbers)
        }
        
        result = operations.get(operation, lambda: None)()
        
        if result is None:
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