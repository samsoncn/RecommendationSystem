import java.util.LinkedList;

public class Delivery extends User {

    private int userId;
    private String userName;
    private LinkedList frds;

    private boolean withDelivery;

    public Delivery(int userId, String userName, LinkedList frds, boolean withDelivery) {
        super(userId, userName, frds);
        this.withDelivery = withDelivery;
    }

    public boolean isWithDelivery() {
        return withDelivery;
    }

    public void setWithDelivery(boolean withDelivery) {
        this.withDelivery = withDelivery;
    }

}
