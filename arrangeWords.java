String input = sentence.substring(0, sentence.length()-1);
    String [] words = input.toLowerCase().split(" ");
    StringBuilder sb = new StringBuilder();
    
    Arrays.sort(words, new java.util.Comparator<String>() {
    @Override
    public int compare(String s1, String s2) {
        return s1.length() - s2.length();
        }
    });
    
    
    for (String word: words) {
        sb.append(word + " ");
    }
    
    String res = sb.substring(0,1).toUpperCase() + sb.substring(1).trim() + ".";
    
    return res; 