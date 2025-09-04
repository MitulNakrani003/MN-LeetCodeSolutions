class Solution {
    public boolean isValid(String s) {
        Stack<Character> parStack = new Stack<>();
        Set<Character> openset = Set.of('{', '(', '[');
        Set<Character> closeset = Set.of('}',')',']');
        for(int i = 0; i < s.length(); i++)
        {
            char current = s.charAt(i);
            if(openset.contains(current))
            {
                parStack.push(current);
            }
            else
            {
                if(parStack.empty())
                {
                    return false;
                }
                if(current == '}')
                {
                    if(parStack.peek() == '{')
                    {
                        System.out.println("Popped: " + parStack.pop());
                    }
                    else
                    {
                        return false;
                    }
                }
                else if(current == ')')
                {
                    if(parStack.peek() == '(')
                    {
                        System.out.println("Popped: " + parStack.pop());
                    }
                    else
                    {
                        return false;
                    }
                }
                else if(current == ']')
                {
                    if(parStack.peek() == '[')
                    {
                        System.out.println("Popped: " + parStack.pop());
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }
        if(parStack.isEmpty())
        {
            return true;
        }
        return false;
    }
}