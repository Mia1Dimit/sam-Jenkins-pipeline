import json
import logging

logger = logging.getLogger()
logger.setLevel('INFO')

def lambda_handler(event, context):
    try:
        # Get input from API Gateway
        body = json.loads(event['body'])
        input_text = body['input']
        
        logger.info(f"Processing input: {input_text}")
        
        # Business logic
        result = input_text.upper()
        
        # Response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'result': result,
                'operation': 'uppercase'
            })
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }