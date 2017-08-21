# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import sys
import traceback
from django.core import mail
from django.views.debug import ExceptionReporter


def send_emailtemplate(subject, from_email, to, text_content,
                       context, html_file, bcc=None):
    msg = EmailMultiAlternatives(subject, text_content, from_email, to, bcc)
    msg.encoding = "utf-8"
    msg.content_subtype = "html"
    try:
        html_content = render_to_string(html_file, context)
        msg.attach_alternative(html_content, "text/html")
    except:
        pass
    msg.send()


def send_manually_exception_email(request, e):
    exc_info = sys.exc_info()
    reporter = ExceptionReporter(request, is_email=True, *exc_info)
    subject = e.message.replace('\n', '\\n').replace('\r', '\\r')[:989]
    message = "%s\n\n%s" % (
        '\n'.join(traceback.format_exception(*exc_info)),
        reporter.filter.get_request_repr(request)
    )
    mail.mail_admins(
        subject, message, fail_silently=True,
        html_message=reporter.get_traceback_html()
    )