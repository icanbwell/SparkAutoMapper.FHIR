class FhirDateTimeFormat:
    date_format: str = "yyyy-MM-dd"
    date_time_format: str = "yyyy-MM-dd'T'kk:mm:ss'Z'"
    date_time_format_no_milliseconds: str = "yyyy-MM-dd'T'hh:mm:ss'Z'"
    time_format: str = "kk:mm:ss"
    time_format_no_milliseconds: str = "hh:mm:ss"
    instant_format: str = "yyyy-MM-dd'T'hh:mm:ss'Z'"
