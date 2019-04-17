

import json
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import Workflow

app = ClarifaiApp(api_key='f721938da77f4cd8b508f8fe61265812')

workflow = Workflow(app.api, workflow_id="workflow-1")

# model = app.models.get('demographics')

# BY URL
image = ClImage(url='https://samples.clarifai.com/demographics.jpg')
response = workflow.predict([image])




# BY LOCAL FILE
# image = model.predict_by_filename('/home/user/image.jpeg')
# response = model.predict_by_filename('/home/user/image.jpeg')


print(json.dumps(response, sort_keys=True, indent=1))
