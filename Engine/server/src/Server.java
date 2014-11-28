import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.HashMap;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import tuple.Tuple;

public class Server{
	public static void main (String[] args) throws FileNotFoundException{
		FileInputStream fstream;
		BufferedReader br;
		String strLine;
		
		HashMap<Integer,String> queries = new HashMap<Integer,String>();
		HashMap<String,Integer> dict = new HashMap<String,Integer>();
		HashMap<Integer,String> links = new HashMap<Integer,String>();
		HashMap<Integer,ArrayList<Tuple>> maps = new HashMap<Integer,ArrayList<Tuple>>();

		System.out.println("Loading....");
		
		/* Reading queries and create query hashmap and dictionary */
		try{
			fstream = new FileInputStream("/home/akhil/NLP/query.txt");
			br = new BufferedReader(new InputStreamReader(fstream));
		
			while( ( strLine = br.readLine() ) != null ){
				String[] data = strLine.split(" : ");
				queries.put(Integer.parseInt(data[0]),data[1]);
				dict.put(data[1],Integer.parseInt(data[0]));
			}
			
			fstream = new FileInputStream("/home/akhil/NLP/url.txt");
			br = new BufferedReader(new InputStreamReader(fstream));
			while( ( strLine = br.readLine() ) != null ){
				String[] data = strLine.split(" : ");
				links.put(Integer.parseInt(data[0]),data[1]);
			}
			
			fstream = new FileInputStream("/home/akhil/NLP/normalised.txt");
			br = new BufferedReader(new InputStreamReader(fstream));
			int i=0,j=0;
			while( (strLine = br.readLine()) != null ){
				String[] data = strLine.split(" ");
				
				ArrayList<Tuple> urls = new ArrayList<Tuple>();
				
				for(j=0;j<data.length;j++){
					if ( Float.parseFloat(data[j]) != 0.0 ){
						Tuple t = new Tuple(j,Float.parseFloat(data[j]));
						urls.add(t);
					}
				}
				
				maps.put(i, urls);
				i = i + 1;
				Collections.sort(urls,Collections.reverseOrder());
			}
				
			System.out.println( returnResults("mytmobile",dict,maps,links) );

		}
		catch(IOException io){
			io.printStackTrace();
		}
	}
	
	public static String returnResults(String query,HashMap<String,Integer>d, HashMap<Integer,ArrayList<Tuple>>u,HashMap<Integer,String>l){
		String results = "";
		if( d.containsKey(query)){
			int qi = d.get(query);
			ArrayList<Tuple> res = u.get(qi);
			int i = 0;
			for(i=0;i<res.size();i++){
				results = results + l.get(res.get(i).first) + "\n" ;
			}
		}
		else
			results = "No record";
		return results;
	}
}