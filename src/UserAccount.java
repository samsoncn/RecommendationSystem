import java.util.LinkedList;

public class UserAccount {

    private String userName;
    private LinkedList frds;
    private LinkedList favFood;

    public UserAccount(String name, LinkedList frds) {
        this.userName = name;
        this.frds = frds;
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

    public void addFrds(LinkedList frd) {
        this.frds.add(frd);
    }
    
}
