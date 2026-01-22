class Solution:
    def decodeString(self, s: str) -> str:
        def getinternalstring(starr, k):
            j = k
            stack = []
            stack.append(starr[j])
            j+=1
            while len(stack) != 0:
                if starr[j] == '[':
                    stack.append(starr[j])
                elif starr[j] == ']':
                    stack.pop()                   
                j+=1
            substarr = starr[k+1:j-1]
            return substarr, j
        
        def createstr(starr):
            result = []
            i = 0
            num = []
            while i < len(starr):
                print(result)
                if starr[i] in ['0','1','2','3','4','5','6','7','8','9']:
                    num.append(starr[i])
                    i +=1
                elif starr[i] == '[':
                    times = int(''.join(num))
                    num = []
                    substarr, newi = getinternalstring(starr, i)
                    result += (createstr(substarr) * times)
                    i = newi
                else:
                    result.append(starr[i])
                    i+=1
            return result

        charlist=list(s)
        c = createstr(charlist)
        print(c)
        return ''.join(c)
