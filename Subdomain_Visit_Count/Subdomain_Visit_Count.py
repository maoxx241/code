class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #split string on " " to get count and whole domain
        #split string on "." to get subdomains
        #the subdomains need slight modification to fit question parameters
        #add the count to each subdomain (by using hash to keep track)
        #convert the key, value pair into a string and append to list that will be returned as the answer
        
        visit = {}
        for pair in cpdomains:
            count, domain = pair.split(" ")   #count and domain, seperated by whitespace
            
            subs = []
            subs = domain.split(".")          #split the domain
            
            subs[0] = domain                  #redefine the domains according to question
            index   = domain.find(".")
            subs[1] = domain[index+1:]

            
            for d in subs:                    #set the count for each domain/subdomain
                if d not in visit:
                    visit[d]  = int(count)
                else:
                    visit[d] += int(count)
        
        pairs = []                            #create a list of strings from the hashmap
        for s in visit:
            temp = str(visit[s]) + " " + str(s)
            pairs.append(temp)
            
        return pairs