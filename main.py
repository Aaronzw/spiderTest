#-*- coding: utf-8 -*-
import urllib2
import json
import random

import labelFilter
import outToTxt

def searchQuestionByTopic(topicId,sum=1000000,pageSize=10,pageNum=1):
     #  ua_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
     #  虚拟header头部
     headers = [{
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'},{
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'},{
          'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'},{
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'},
          {
     }]
     #  example topicI=19550447
     # #  分页查询页码
     # pageNum=0
     # #  分页查询页大小
     # pageSize=10
     #  查询总数
     cnt=0
     while(True):
          # url1="https://www.zhihu.com/api/v4/topics/"+str(topicId)+"/feeds/essence?include=" \
          #      "data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;" \
          #      "data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;" \
          #      "data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;" \
          #      "data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;" \
          #      "data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=article)].target.annotation_detail,content,hermes_label,is_labeled,author.badge[?(type=best_answerer)].topics;" \
          #      "data[?(target.type=question)].target.annotation_detail,comment_count;" \
          #      "limit="+str(pageSize)+"&offset="+str(10*pageNum)
          url1="https://www.zhihu.com/api/v4/topics/"+str(topicId)+"/feeds/essence?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit="+str(pageSize)+"&offset="+str(pageSize*pageNum)
          pageNum=pageNum+1
          # 随机header编码，据说防封
          head_No=random.randint(0,len(headers)-1)
          request = urllib2.Request(url1, headers=headers[head_No])

          response = urllib2.urlopen(request)
          #  str
          html = response.read()
          #  unicode
          unicodeStr =json.loads(html)
          if unicodeStr['paging']['is_end'] :
               break
          data = unicodeStr['data']
          for item in data:
               if(item["target"].has_key("question")):  # 结果里可能包含文章，不是question,排除
                    qid = item["target"]["question"]["id"]
                    title=item["target"]["question"]["title"]
                    top_answer=item["target"]["content"]
                    outToTxt.outTxt(title.encode('utf-8'))
                    outToTxt.outTxt(labelFilter.html_filter(top_answer.encode('utf-8')))
                    cnt=cnt+1
          print cnt
          if(cnt>sum):
               return
     print cnt

searchQuestionByTopic(19550447,sum=10000)






