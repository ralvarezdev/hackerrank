import java.io.*;
import java.util.*;

public class Solution {
    public  static String setFirstUpperCase(String word)
    {
        return Character.toUpperCase(word.charAt(0))+ word.substring(1);
    }

    public static void main(String[] args) {
        Scanner scanner= new Scanner(System.in);
        boolean isSplit;
        Character SPLIT='S', CLASS='C', VARIABLE='V', METHOD='M',typeWord;
        
        while(scanner.hasNext()){   
            String[] line=scanner.nextLine().split(";");
            isSplit=SPLIT.equals(line[0].charAt(0));
            typeWord=line[1].charAt(0);
            String formattedStr="";
            String[] words = line[2].split(" ");
                        
            if(!isSplit){                   
                if(typeWord.equals(CLASS))
                    for(String word: words)
                        formattedStr+=setFirstUpperCase(word);
                
                else{
                    int counter=0;
                    
                    for(String word:words){
                        if(counter!=0)
                           formattedStr+=setFirstUpperCase(word);
                        else
                            formattedStr+=word;
                        
                        counter++;
                    }
                    
                    if(typeWord.equals(METHOD))
                        formattedStr+="()";
                }
            }
            else{            
                int counter=0;
                String word=words[0];
                
                if(typeWord.equals(METHOD))
                    word=word.substring(0, word.length()-2);
                
                for(int i=0;i<word.length();i++){   
                    char letter=word.charAt(i);
                
                    if(counter!=0 && Character.isUpperCase(letter))
                        formattedStr+=' ';
                    
                    formattedStr+=Character.toLowerCase(letter);
                    counter++;
                }
            }            
            System.out.println(formattedStr);
        }
    }
}