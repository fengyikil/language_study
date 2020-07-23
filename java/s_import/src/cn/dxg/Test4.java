package cn.dxg;
import cn.dxg.cal.MyAdd;
public class Test4 {
    public static void main(final String[] args) throws Exception { 
        MyAdd myAdd = new MyAdd();
        double result = myAdd.add(1.6, 1.5);
        System.out.println(result);
    }
}