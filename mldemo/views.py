from django.shortcuts import render

from django.http import HttpResponse

from .models import HomePageProject, Supervised, Unsupervised

import pickle
import numpy as np
import json


# Create your views here.
def index(request):
    homepageprojects = HomePageProject.objects.all()[0:6]
    return render(request, 'mldemo/index.html', {
      'homepageprojects' : homepageprojects
    })


def supervised_category(request):
    supervisedprojectcategorys = Supervised.objects.all()
    return render(request, 'mldemo/supervised.html', {
      'supervisedprojectcategorys' : supervisedprojectcategorys
    })


def unsupervised_category(request):
    unsupervisedprojectcategorys = Unsupervised.objects.all()
    return render(request, 'mldemo/unsupervised.html', {
      'unsupervisedprojectcategorys' : unsupervisedprojectcategorys
    })


def mlprojects(request):
    supervisedprojects = Supervised.objects.all()
    unsupervisedprojects = Unsupervised.objects.all()
    return render(request, 'mldemo/allmlprojects.html', {
      'supervisedprojects' : supervisedprojects,
      'unsupervisedprojects' : unsupervisedprojects
    })


def json_convert(para):
    return json.loads(para)

iris_model = pickle.load(open('models/knn_iris_model.pkl','rb'))
def iris(request):
    result_value = ''
    if request.method == 'POST':
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']

        check_result = iris_model.predict(np.asarray([[json_convert(sepal_length),json_convert(sepal_width),json_convert(petal_length),json_convert(petal_width)]]))

        result_value = "Category of iris flower is "+str(check_result[0])

    return render(request, 'mldemo/iris_classification.html', {
      'result_value': result_value
    })


iris_model = pickle.load(open('models/regression_salary_model.pkl','rb'))
def salary(request):
    result_value = ''
    if request.method == 'POST':
        year_of_exp = request.POST['year_of_exp']

        check_result = iris_model.predict(np.asarray([[json_convert(year_of_exp)]]))

        result_value = "The best salary you should offer to him/her is Rs."+str(int(check_result[0]))

    return render(request, 'mldemo/salary_regression.html', {
      'result_value': result_value
    })
