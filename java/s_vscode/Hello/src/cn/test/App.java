

import netscape.javascript.JSObject;
import org.json.JSONObject;

public class App {
    public static void main(String[] args) throws Exception {
        // System.out.println("Hello, World!");
        // Scanner sc = new Scanner(System.in);
        // int a = sc.nextInt();
        // int b = sc.nextInt();
        // System.out.println(a + b);
        // sc.close();
        JSONObject jsonObject = new JSONObject();

        jsonObject.append("key1",88);
        jsonObject.append("key2","xxx");
        System.out.println(jsonObject.toString());
    }
}
