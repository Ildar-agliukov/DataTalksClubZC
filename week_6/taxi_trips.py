import faust


class GreenTaxiTrip(faust.Record):
    vendorid: str
    lpep_pickup_datetime: str
    lpep_dropoff_datetime: str
    store_and_fwd_flag: str
    ratecodeid: str
    pulocationid: str
    dolocationid: str
    passenger_count: str
    trip_distance: str
    fare_amount: str
    extra: str
    mta_tax: str
    tip_amount: str
    tolls_amount: str
    ehail_fee: str
    improvement_surcharge: str
    total_amount: str
    payment_type: str
    trip_type: str
    congestion_surcharge: str

class FhvTaxiTrip(faust.Record):
    dispatching_base_num: str
    pickup_datetime: str
    dropoff_datetime: str
    pulocationid: str
    dolocationid: str
    sr_flag: str
    affiliated_base_number: str