## Data Pipelines
- AWS Lambda + Stepfunctions
- Lambad function 
    - trigger
    - function
    - 
- boiler plate code  (Lambda function)
    ```
    import json

    def lambda_handler(event, context)
        # TODO implement
        return{
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
    ```
## Step Function
- Lambda 1 -> output -> (input to) Lambda 2
- to chain the functions -> Step Function

## Query Databricks Pipeline
- Azure databricks
- 