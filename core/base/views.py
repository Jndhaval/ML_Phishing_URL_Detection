import numpy as np
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .feature import FeatureExtraction

file = open("C:\\Users\\Stazzy\\Desktop\\FinalYear\\core\\base\\model.pkl", "rb")
gbc = pickle.load(file)
file.close()

@api_view(['POST'])
def predict(request):
    url = request.data.get('url', '')
    print(request.data)
    if not url:
        return Response({'error': 'URL is required'}, status=400)

    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1, 30)

    y_pred = gbc.predict(x)[0]
    y_pro_phishing = gbc.predict_proba(x)[0, 0]
    y_pro_non_phishing = gbc.predict_proba(x)[0, 1]

    response_data = {
        'url': url,
        'prediction': y_pred,
        'probability_phishing': y_pro_phishing,
        'probability_non_phishing': y_pro_non_phishing
    }
    return Response(response_data)
