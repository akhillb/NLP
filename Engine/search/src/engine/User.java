package engine;
import java.util.ArrayList;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.HashMap;

public class User {
	private ArrayList<String> history;
	private HashMap<Integer,String> qs;
	private HashMap<String,Integer> dict;
	private HashMap<Integer,String> url;
	
	public User(){
		history = new ArrayList<String>();
		qs = new HashMap<Integer,String>();
		dict = new HashMap<String,Integer>();
		url = new HashMap<Integer,String>();
	}
	
	public User(HashMap<Integer,String>q,HashMap<String,Integer>d,HashMap<Integer,String>l){
		history = new ArrayList<String>();
		qs = q;
		dict = d;
		url = l;
	}
	
	public String getResults(String query){
		history.add(query);
		if (dict.containsKey(query))
			query = "hello";
		return query;
	}
}
