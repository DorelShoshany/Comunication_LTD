export class PackageOfferring {
    public name;
    public price;
    public id;


    constructor(rawData) {
        this.name = rawData.name;
        this.price = rawData.price;
        this.id = rawData.id;
    }
}
