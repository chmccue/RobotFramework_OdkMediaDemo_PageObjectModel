import requests, sys
from pprint import pprint

#iPhone 7+ with iOS 10.2.1
mobile_header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1'}

class GlobalCustomWebScraper(object):
    
    def __init__(self):
        object.__init__(self)
        self.fail_dict = {}
        self.js_dict = {}
        self.fail_count = 0
        self.js_count = 0
        self.payload = {}

    def update_payload(self, **kwargs):
        self.payload.update(kwargs)
        return self.payload

    def assert_404_not_in_status_path(self, req):
        '''
        Documentation: function takes a request library get request.
        
        example: assert "404" not in str(_request_.history)
        checks status code path history for any possible redirects that 
        may have gone to a 404 error. Numbers are converted to strings 
        for assertion.
        '''
        assert "404" not in str(req.history)
        assert "404" not in str(req.status_code)

    def clean_up_list(self, base_url, *url_list):
        ready_list = []
        for url in url_list:
                    
            if "http" not in url[0:4] and "//" not in url[0:2]:
                url_ready = base_url + url
            elif "http" not in url[0:4] and "//" in url[0:2]:
                url_ready = "http:" + url
            else:
                url_ready = url
                
            ready_list.append(url_ready)
        #print ready_list
        #sort_list = ready_list.sort()
        sorted_list = sorted(set(ready_list))
        return sorted_list

    def check_data_url(self, base_url, *url_list, **custom_payload):
        fail_count = self.fail_count
        js_count = self.js_count
        self.update_payload(**custom_payload)
        count = 0
        dropped_login_count = 0
        forbidden_link_dict = {}
        forbidden_link_count = 0
                
        # Use 'with' to ensure the session context is closed after use.
        with requests.Session() as s:
            '''
            pass payload to post request to log into site. See below logic for
            reconnecting login in case the connection gets dropped.
            '''
            s.post(base_url, data=self.payload, verify=True)
            sorted_list = self.clean_up_list(base_url, *url_list)
            
            for url in sorted_list:
                
                try:
                    if ".js" in url or "javascript:" in url:
                        js_count += 1
                        self.js_dict.update({js_count: str(url)})
                        continue
                    
                    r = s.get(url)
                    # ====================
                    check_new_url = r.url
                    if "passthru=" in str(check_new_url):
                        '''
                        if the https connection goes down, this will reset it
                        by passing payload to post request to log into site again.
                        '''
                        s.post(base_url, data=self.payload, verify=True)
                        #print "\npayload login credentials added.\n"
                        r = s.get(url)
                        check_new_url = r.url
                        dropped_login_count += 1
                        
                    print "\nurl entered:  %s\nurl returned: %s\n" %(url, check_new_url)
                    # ====================
                    check_status_code = r.status_code
                    check_status_code_history = r.history
                    # ====================
                    try:
                        if "403" != str(check_status_code):
                            count += 1
                            self.assert_404_not_in_status_path(r)
                        else:
                            forbidden_link_count += 1
                            forbidden_link_dict.update({forbidden_link_count: [str(url), "status code: " + str(check_status_code)]})
                    except Exception, e:
                        #print('\nError on line {}'.format(sys.exc_info()[-1].tb_lineno))
                        #print type(e)
                        #print e
                        #print "\nassert_status_codes = False"
                        fail_count += 1
                        self.fail_dict.update({fail_count: 
                                               ["url entered:  "+ str(url), 
                                                "url returned: " + str(check_new_url), 
                                                check_status_code, check_status_code_history]})
                        
                except Exception, e:
                    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
                    print type(e)
                    print e
                    
            # ====================
            print "\nSkipped Javascript links:"
            pprint(self.js_dict)
            print "\nSkipped 403 Forbidden status code links:"
            pprint(forbidden_link_dict)
            print "\nDropped login connection count: %d" %dropped_login_count
            print "\n\n"
            print "Total number of URLs checked: " + str(count)
            print "\n\n"
            # ====================
            if len(self.fail_dict) > 0:
                print "Failed link information:"
                pprint(self.fail_dict)
                self.custom_delete_all_dict_items(self.fail_dict)
                return False
            else: return True
    
    def custom_delete_all_list_items(self, list_to_empty):
        del list_to_empty[:]
        return list_to_empty

    def custom_delete_all_dict_items(self, dict_to_empty):
        dict_to_empty.clear()
        return dict_to_empty
