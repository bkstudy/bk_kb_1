# coding: utf8
 
import json
from common.log import logger
from common.mymako import render_mako_context
from meeting.models import meetingRecord
from django.core.context_processors import csrf

# from django.shortcuts import render
# from django.template import RequestContext
# from django.http import HttpResponse
# from django.shortcuts import render_to_response
# import pdb

# Create your views here.

def getJson(request):
    rs = meetingRecord.objects.all()
    jsonData = []
    for r in rs:
        result = {}
        result['id'] = r.id
        result['theme'] = r.theme
        result['content'] = r.content
        result['oper'] = r.oper
        result['add_time'] = str(r.add_time)
        jsonData.append(result)
    js = json.dumps({"items":jsonData}, ensure_ascii=False)
    return render_mako_context(request, "meeting/json.html", {"msg":js})

    
def home(request):
    rs = meetingRecord.objects.all()
    logger.info("whc got data:{}".format(str(rs)))
    return render_mako_context(
        request,
        "/meeting/home.html",
        {"adm":"whc["+request.user.username+"]", "rs":rs,
            "csrf_token":csrf(request)["csrf_token"]
        },
    )
'''
    return render_to_response(
        template_name="/meeting/home.html",
        dictionary={"adm":"whc["+request.user.username+"]", "rs":rs},
        context_instance=RequestContext(request)
    )
'''

def save(request):
    #pdb.set_trace()
    theme = request.POST["theme"]
    content = request.POST["content"]
    msg = u"录入会议失败！"
    if theme:
        rs = meetingRecord(theme=theme, content=content,oper=request.user.username)
        rs.save()
        msg = u"录入会议成功！"
    return render_mako_context(request, "/meeting/json.html", {"msg":msg})