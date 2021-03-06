from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from auto_survey.views.surveys import redirects_twilio_request_to_proper_endpoint
from auto_survey.views.surveys import redirect_to_first_results
from auto_survey.views.questions import show_question
from auto_survey.views.surveys import show_survey, show_survey_results
from auto_survey.views.question_responses import save_response

urlpatterns = [
    url(r'^$', redirect_to_first_results, name='app_root'),

    url(r'^survey/(?P<survey_id>\d+)/question/(?P<question_id>\d+)$',
        show_question,
        name='question'),

    url(r'^survey/(?P<survey_id>\d+)$',
        show_survey,
        name='survey'),

    url(r'^first-survey/',
        csrf_exempt(redirects_twilio_request_to_proper_endpoint),
        name='first_survey'),

    url(r'^survey/(?P<survey_id>\d+)/results$',
        show_survey_results,
        name='survey_results'),

    url(r'^survey/(?P<survey_id>\d+)/question/(?P<question_id>\d+)/question_response$',
        csrf_exempt(save_response),
        name='save_response')
]