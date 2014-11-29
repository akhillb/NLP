import java.io.*;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.HashMap;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import tuple.Tuple;
import java.io.DataOutputStream;
import java.net.*;
import edu.cmu.lti.lexical_db.ILexicalDatabase;
import edu.cmu.lti.lexical_db.NictWordNet;
import edu.cmu.lti.ws4j.RelatednessCalculator;
import edu.cmu.lti.ws4j.impl.WuPalmer;


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
			String dir = "/home/akhil/NLP/testing/";
			fstream = new FileInputStream(dir + "query.txt");
			br = new BufferedReader(new InputStreamReader(fstream));
		
			while( ( strLine = br.readLine() ) != null ){
				String[] data = strLine.split(" : ");
				queries.put(Integer.parseInt(data[0]),data[1]);
				dict.put(data[1],Integer.parseInt(data[0]));
			}
			
			fstream = new FileInputStream(dir + "url.txt");
			br = new BufferedReader(new InputStreamReader(fstream));
			while( ( strLine = br.readLine() ) != null ){
				String[] data = strLine.split(" : ");
				links.put(Integer.parseInt(data[0]),data[1]);
			}
			
			fstream = new FileInputStream(dir + "normalised.txt");
			br = new BufferedReader(new InputStreamReader(fstream));
			int i=0,j=0;
			while( (strLine = br.readLine()) != null ){
				String[] data = strLine.split(" ");
				
				ArrayList<Tuple> urls = new ArrayList<Tuple>();
				
				for(j=0;j<data.length;j++){
					String[] edges = data[j].split(",");
					Tuple t = new Tuple(Integer.parseInt(edges[0]),Float.parseFloat(edges[1]));
					urls.add(t);
				}
				
				maps.put(i, urls);
				i = i + 1;
				Collections.sort(urls,Collections.reverseOrder());
			}
			System.out.println("Finished loading data");
			ServerSocket sersock = new ServerSocket(3000); 
			System.out.println("Server ready..");
			Socket sock = sersock.accept( ); // reading from keyboard (keyRead object) 
			InputStream istream = sock.getInputStream(); 
			OutputStream os = sock.getOutputStream();
	        OutputStreamWriter osw = new OutputStreamWriter(os);
			BufferedReader receiveRead = new BufferedReader(new InputStreamReader(istream));  
			String receiveMessage, sendMessage; 
			while(true) { 
				if((receiveMessage = receiveRead.readLine()) != null) 
				{ 
					System.out.println("Received Query: "+ receiveMessage); 
					sendMessage = returnResults(receiveMessage,dict,maps,links); 
					DataOutputStream out = new DataOutputStream(sock.getOutputStream());
					out.writeBytes(sendMessage);
	                System.out.println("Message sent to the client is "+sendMessage);
				}
				} 
		}
		catch(IOException io){
			io.printStackTrace();
		}
	}
	
	public static String returnResults(String query,HashMap<String,Integer>d, HashMap<Integer,ArrayList<Tuple>>u,HashMap<Integer,String>l){
		String results = "No record;";
		if( d.containsKey(query)){
			results = "";
			int qi = d.get(query);
			ArrayList<Tuple> res = u.get(qi);
			System.out.println(res);
			int i = 0;
			for(i=0;i<res.size();i++){
				results = results + l.get(res.get(i).first) + " " ;
			}
		}
		else{
			ILexicalDatabase db = new NictWordNet();
			RelatednessCalculator wup = new WuPalmer(db);
			double sim1 = wup.calcRelatednessOfWords("","");
		}
		System.out.println(results);
		return results+"\n";
	}
}