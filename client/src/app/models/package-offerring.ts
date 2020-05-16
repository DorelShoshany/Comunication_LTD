export class PackageOfferring {
    public name;
    public price;

    constructor(rawData) {
        this.name = rawData.name;
        this.price = rawData.price;
    }
}
