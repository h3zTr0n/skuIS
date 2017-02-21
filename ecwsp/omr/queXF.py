from django.conf import settings
import urllib, urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import MySQLdb

def import_queXF(pdf,banding,test_id):
        register_openers()
        url = '%s/admin/new.php' % (settings.QUEXF_URL,)
        description = str(test_id)

        values = {'form':open(pdf, 'r'),
                  'bandingxml':open(banding, 'r'),
                  'desc':description
                  }
        data, headers = multipart_encode(values)
        headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        request = urllib2.Request(url, data, headers)
        request.unverifiable = True
        response = urllib2.urlopen(request)
        the_page = response.read()

def pagesetup(qid,pid):
        """
        Run page setup on quexf, this is required for quexf to function. Typically a human would
        do this, but there is no need for interaction.
        qid: Questionairre id for quexf
        pid: page id for quexf
        """
        url = '%s/admin/pagesetup.php?zoom=3&pid=%s&qid=%s&done=done' % (settings.QUEXF_URL,pid,qid)
        response = urllib2.urlopen(url)
