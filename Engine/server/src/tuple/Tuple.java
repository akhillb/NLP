package tuple;

public class Tuple implements Comparable<Tuple>{
	public Integer first;
	public Float second;
	
	public Tuple(){
		first = 0;
		second = Float.valueOf("0.0");
	}
	
	public Tuple(Integer a,Float f){
		first = a;
		second = f;
	}

	@Override
	public int compareTo(Tuple o) {
		// TODO Auto-generated method stub
		return this.second.compareTo(o.second);
	}
	
	public String toString(){
		return "("+this.first.toString()+","+this.second.toString()+")";
	}
}
	

