 /**
 * The Shop class represents a shop that employs sales consultants and marketing specialists.
 * It keeps track of the workers and their turnover.
 */
public class Shop {
    private static Shop instance;
    private List<Object> workers = new ArrayList<>();

    /**
     * Returns an instance of the Shop class.
     */
    public static Shop getInstance() {
        if (instance == null) {
            instance = new Shop();
        }
        return instance;
    }

    /**
     * Adds a worker to the list of workers.
     */
    public void addWorker(Object worker) {
        this.workers.add(worker);
    }

    /**
     * Returns total turnover.
     */
    public double getTurnover() {
        double turnOver = 0.0;
        for (Object worker : this.workers) {
            if (worker instanceof SalesConsultant) {
                turnOver += ((SalesConsultant) worker).getMoney();
            }
            if (worker instanceof MarketingSpecialist) {
                turnOver += ((MarketingSpecialist) worker).getBudget();
            }
        }
        return turnOver;
    }
}

/**
 * The SalesConsultant class represents a sales consultant employed by the shop.
 * It keeps track of the shop they work for, and the money they have earned from selling products.
 */
public class SalesConsultant {
    private Shop workingShop;
    private double earnedMoney = 0.0;

    /**
     * Creates a new SalesConsultant instance and adds it to the list of workers.
     */
    public SalesConsultant() {
        this.workingShop = Shop.getInstance();
        this.workingShop.addWorker(this);
    }

    /**
     * Sells a product and adds the price to the earned money.
     */
    public void sellProduct(double price) {
        this.earnedMoney += Math.max(price, 0);
    }

    /**
     * Returns the amount of money the sales consultant has earned.
     */
    public double getMoney() {
        return this.earnedMoney;
    }
}

/**
 * The MarketingSpecialist class represents a marketing specialist employed by the shop.
 * It keeps track of the shop they work for, and the budget they have available for marketing campaigns.
 */
public class MarketingSpecialist {
    private Shop workingShop;
    private double budget;

    /**
     * Creates a new MarketingSpecialist with the specified budget, and adds it to the list of workers.
     */
    public MarketingSpecialist(double budget) {
        this.budget = budget;
        this.workingShop = Shop.getInstance();
        this.workingShop.addWorker(this);
    }

    /**
     * Spends money on a marketing campaign.
     * Throws an IllegalArgumentException if the campaign cost is negative or exceeds the budget.
     */
    public void spendMoney(double marketingCampaignCost) {
        if (marketingCampaignCost < 0) {
            throw new IllegalArgumentException("Marketing campaign cost cannot be negative");
        }
        if (marketingCampaignCost > budget) {
            throw new IllegalArgumentException("Marketing campaign cost exceeds budget");
        }
        this.budget -= marketingCampaignCost;
    }

    /**
     * Returns the budget available for marketing campaigns.
     */
    public double getBudget() {
        return this.budget;
    }
}
