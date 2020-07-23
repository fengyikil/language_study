package cn.dxg;

import org.json.JSONObject;

public class Test3 {
   
    public static void main(final String[] args) throws Exception {
        final JSONObject jsonObject = new JSONObject();
        jsonObject.append("key1",88);
        jsonObject.append("key2","xxx");
        System.out.println(jsonObject.toString());
    } 
}