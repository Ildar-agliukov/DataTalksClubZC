import faust

from taxi_trips import GreenTaxiTrip, FhvTaxiTrip



app = faust.App('pulocation_count', broker='kafka://localhost:9092')
green = app.topic('green_taxi', value_type=GreenTaxiTrip)
fhv = app.topic('fhv_taxi', value_type=FhvTaxiTrip)


pulocationid = app.Table('pulocationid', default=int)

@app.agent(green)
async def green_reading(stream):
    async for event in stream.group_by(GreenTaxiTrip.pulocationid):
        pulocationid[event.pulocationid] += 1

@app.agent(fhv)
async def green_reading(stream):
    async for event in stream.group_by(FhvTaxiTrip.pulocationid):
        pulocationid[event.pulocationid] += 1


if __name__ == '__main__':
    app.main()