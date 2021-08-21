import java.util.LinkedList;

public class User {

    private int userId;

    private String userName;
    private LinkedList frds;


    public User(int userId, String name) {
        this.userId = userId;
        this.userName = name;
        this.frds = null;
    }

    public User(int userId, String name, LinkedList frds) {
        this.userId = userId;
        this.userName = name;
        this.frds = frds;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public LinkedList getFrds() {
        return frds;
    }

    public void setFrds(LinkedList frds) {
        this.frds = frds;
    }

    public void addFrds(LinkedList frds) {
        this.frds.add(frds);
    }

    
    
}
