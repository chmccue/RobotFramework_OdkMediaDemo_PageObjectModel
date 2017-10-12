import re



class GlobalCustomRegex(object):
    
    
    def custom_search_for_regex(self, text_to_search, regex_to_find):
        
        self.prep_compile_regex = re.compile(regex_to_find)
        self.mo = self.prep_compile_regex.search(text_to_search)
        
        return self.mo.group()[0:-1]



    def split_string_using_regex(self, string, delimiters=(", ", ","), maxsplit=0):
        '''
        Documentation: this function takes an element locator string and will remove the 
        jquery/css tag at the start of it, and any bundled locators (different locators 
        separated by commas in a single locator variable) will be returned as separate 
        locators, returning them in a list format.
        
        For example: if you have an element locator such as "jquery=.hello, .world" where
        the 2 locators ".hello" and ".world" are bundled together, this function will
        remove the jquery= tag and return the string in list format of [.hello, .world],
        which can then be used to iterate through in a for loop and use each single 
        locator on its own.
        
        >>>split_string_using_regex("jquery=.hello, .world")
        >>>[".hello", ".world"]
        Then can be used by themselves in a for loop:
        >>>for i in lst:
        >>>    print i
        >>>.hello
        >>>.world
        '''
        self.string_tag_removed = re.sub(r'(?i)(jquery|css)=', '', string)
        self.regexPattern = '|'.join([re.escape(x) for x in delimiters])
        
        return re.split(self.regexPattern, self.string_tag_removed, maxsplit)
        
    
    #def count_number_of_regex_found(self, regex, text_to_search):
    #    self.regex_find_all = re.findall(regex, text_to_search)
    #    return len(self.regex_find_all)
        

    def string_should_only_appear_once(self, regex, text_to_search):
        
        '''
        Documentation: This function takes a regular expression as an argument, and 
        text to search for the other argument. If any matches of the regular expression 
        are found in the text to search, they are stored in a list.
        
        If more than 1 item in the newly created list,
        for loop and nested loop go through each item and compare them against 
        each other. If there is a duplicate match found, the variable 
        "match count" gets an additional 1 and is reported as a fail,
        with fail details and the list that the function was checking, 
        so a person can verify the list items themselves."
        '''
        
        match_found = False
        match_count = 0
        
        self.regex_find_all = re.findall(regex, text_to_search)
        self.regex_count = len(self.regex_find_all)
        
        if self.regex_count > 1:
            for match in self.regex_find_all:
                for num_count in range(self.regex_count):
                    print "checking " + match + " against " + self.regex_find_all[num_count-1]
                
                    if match in self.regex_find_all[num_count-1]:
                        match_count += 1

                if match_count <= 1:
                    # Below resets match_count for start of next item in list to be counted in the loop.
                    match_count = 0
                ''' More than 1 match, because each list should have at least 1 counted match 
                 (when the item in the list is matched against itself in the list). '''
                if match_count > 1:
                    match_found = True
                    break
        
        if match_found == True:
            print "Match found in text"
            print str(self.regex_find_all)
            return False
        if match_found == False:
            print "No matches found."
            print str(self.regex_find_all)
            return True
        







            
