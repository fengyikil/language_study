package cn.dxg;

import org.json.JSONObject;

import cn.dxg.cal.*;
public class Test7 {
    public static void main(final String[] args) throws Exception { 
        MyAdd myAdd = new MyAdd();
        double result = myAdd.add(1.6, 1.5);
        System.out.println(result);

        MySub mySub = new MySub();
        result = mySub.sub(3, 1.5);
        System.out.println(result);

        MyMul myMul = new MyMul();
         result = myMul.mul(12, 12);
        System.out.println(result);

        MyDiv myDiv = new MyDiv();
        result = myDiv.div(12, 2);
        System.out.println(result);

        final JSONObject jsonObject = new JSONObject();
        jsonObject.append("key1",88);
        jsonObject.append("key2","xxx");
        System.out.println(jsonObject.toString());
    }
}