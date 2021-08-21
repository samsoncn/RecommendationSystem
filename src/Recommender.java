import java.util.LinkedList;

public class Recommender extends User{

    private int userId;
    private String userName;
    private LinkedList frds;

    private int id;
    private String categories;
    private String name;
    private int popularity;
    private int calories;
    private int like;
    private int nope;

    public Recommender(int userId, String userName, LinkedList frds, int id, String categories, String name,
                       int popularity, int calories, int like, int nope){

        super(userId, userName, frds);

        this.id = id;
        this.categories = categories;
        this.name = name;
        this.popularity = popularity;
        this.calories = calories;
        this.like = like;
        this.nope = nope;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getCategories() {
        return categories;
    }

    public void setCategories(String categories) {
        this.categories = categories;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPopularity() {
        return popularity;
    }

    public void setPopularity(int popularity) {
        this.popularity = popularity;
    }

    public int getCalories() {
        return calories;
    }

    public void setCalories(int calories) {
        this.calories = calories;
    }

    public int getLike() {
        return like;
    }

    public void setLike(int like) {
        this.like = like;
    }

    public int getNope() {
        return nope;
    }

    public void setNope(int nope) {
        this.nope = nope;
    }

    public void addLike() {
        this.like += 1;
    }

    public void addNope() {
        this.nope += 1;
    }

    

}