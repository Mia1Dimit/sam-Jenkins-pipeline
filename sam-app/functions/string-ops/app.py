import json

def lambda_handler(event, context):
    try:
        # Get query parameters from API Gateway
        query_params = event.get('queryStringParameters', {})
        text = query_params.get('text', '')
        operation = query_params.get('op', 'length')
        
        operations = {
            'length': len(text),
            'words': len(text.split()),
            'reverse': text[::-1],
            'lower': text.lower(),
            'upper': text.upper(),
            'title': text.title()
        }
        
        result = operations.get(operation, "Invalid operation")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'result': result,
                'original': text,
                'operation': operation
            })
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }