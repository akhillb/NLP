import edu.cmu.lti.lexical_db.ILexicalDatabase;
import edu.cmu.lti.lexical_db.NictWordNet;
import edu.cmu.lti.ws4j.RelatednessCalculator;
import edu.cmu.lti.ws4j.impl.WuPalmer;
import engine.User;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import engine.User;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.ArrayList;

public class Main{
	public static void main(String [] args) throws FileNotFoundException{
		try{
			String query;
			boolean stop = false;
			HashMap<Integer,String> queries = new HashMap<Integer,String>();
			HashMap<Integer,String> links = new HashMap<Integer,String>();
			HashMap<String,Integer> dictionary = new HashMap<String,Integer>();
			HashMap<Integer,ArrayList<Integer>> maps = new HashMap<Integer,ArrayList<Integer>>();
			System.out.println("Loading....");

			FileInputStream fstream = new FileInputStream("/home/akhil/NLP/data/query.txt");
			BufferedReader br1 = new BufferedReader(new InputStreamReader(fstream));
			String strLine;
			while( (strLine = br1.readLine()) != null ){
				String [] data = strLine.split(" : ");
				queries.put(Integer.parseInt(data[0]), data[1]);
				dictionary.put(data[1],Integer.parseInt(data[0]));
			}
			
			fstream = new FileInputStream("/home/akhil/NLP/data/url.txt");
			br1 = new BufferedReader(new InputStreamReader(fstream));
			while( (strLine = br1.readLine()) != null ){
				String [] data = strLine.split(" : ");
				links.put(Integer.parseInt(data[0]), data[1]);
			}	
			
			fstream = new FileInputStream("/home/akhil/NLP/data/normalised.txt");
			br1 = new BufferedReader(new InputStreamReader(fstream));
			int i = 0,j=0;
			while( (strLine = br1.readLine()) != null ){
				String [] data = strLine.split(" ");
			}

			System.out.println("Enter your search queries");
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

			User user = new User(queries,dictionary,links);
			while( !stop ){
				System.out.print("> ");
				if((query=br.readLine()) != null){
					String results = user.getResults(query);
					System.out.println(results);
				}
				else
					stop = true;
			}
			System.out.println("\nBye...");
		}
		catch(IOException e){
			e.printStackTrace();
		}
	}
}
