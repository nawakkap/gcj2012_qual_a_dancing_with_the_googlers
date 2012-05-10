for T in range(1, int(raw_input())+1) :
    case_input = raw_input().split(' ')
    N = int(case_input.pop(0))
    S = int(case_input.pop(0))
    p = int(case_input.pop(0))
    #print "#Googlers = %d, #surprise = %d, best = %d" %(N,S,p)
    
    maxbestscore = 0
    for t in range(0, N) :
        if int(case_input[t]) < p :
            maxbestscore = maxbestscore
            #print "input:%s -> [triplets<p] Max best score no  + 0" %case_input[t]
        elif int(case_input[t]) - p>= p*2 -2 :
            #print "input:%s -> Max best score no  + 1" %case_input[t]
            maxbestscore += 1
        elif int(case_input[t]) - p< p*2-2 and int(case_input[t])-p >= p*2-4 and S > 0 :
            maxbestscore += 1
            S -= 1
            #print "input:%s -> Max best score no  + 1 (surprise case), surprise case left = %d" %(case_input[t],S)
        else :
            maxbestscore = maxbestscore
            #print "input:%s -> [triplets<3*p-2 and no surprise case] Max best score no  + 0" %case_input[t]
            
    #print 'Surprising case left: %d' %S        
    print 'Case #%d: %d' % (T, maxbestscore)
    #print '=========================================================='
    
            
            
            
            
        
        
    