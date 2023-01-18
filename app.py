from flask import Flask, jsonify, request
from kerykeion import KrInstance
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    user_input = request.get_json()

    year = user_input['year']
    month = user_input['month']
    day = user_input['day']
    hour = user_input['hour']
    minute = user_input['minute']
    location = user_input['location']

    if(request.method == 'POST'):

        user_chart = KrInstance("Danilo", year, month, day, hour, minute, location)

        planets = {
            1: {"sun_sign": user_chart.sun['sign'], "sun_position": round(user_chart.sun['position'], 3), "sun_house": user_chart.sun['house'], "sun_retrograde": user_chart.sun['retrograde']},
            2: {"moon_sign": user_chart.moon['sign'], "moon_position": round(user_chart.moon['position'], 3), "moon_house": user_chart.moon['house'], "moon_retrograde": user_chart.moon['retrograde']},
            3: {"mercury_sign": user_chart.mercury['sign'], "mercury_position": round(user_chart.mercury['position'], 3), "mercury_house": user_chart.mercury['house'], "mercury_retrograde": user_chart.mercury['retrograde']},
            4: {"venus_sign": user_chart.venus['sign'], "venus_position": round(user_chart.venus['position'], 3), "venus_house": user_chart.venus['house'], "venus_retrograde": user_chart.venus['retrograde']},
            5: {"mars_sign": user_chart.mars['sign'], "mars_position": round(user_chart.mars['position'], 3), "mars_house": user_chart.mars['house'], "mars_retrograde": user_chart.mars['retrograde']},
            6: {"jupiter_sign": user_chart.jupiter['sign'], "jupiter_position": round(user_chart.jupiter['position'], 3), "jupiter_house": user_chart.jupiter['house'], "jupiter_retrograde": user_chart.jupiter['retrograde']},
            7: {"saturn_sign": user_chart.saturn['sign'], "saturn_position": round(user_chart.saturn['position'], 3), "saturn_house": user_chart.saturn['house'], "saturn_retrograde": user_chart.saturn['retrograde']},
            8: {"uranus_sign": user_chart.uranus['sign'], "uranus_position": round(user_chart.uranus['position'], 3), "uranus_house": user_chart.uranus['house'], "uranus_retrograde": user_chart.uranus['retrograde']},
            9: {"neptune_sign": user_chart.neptune['sign'], "neptune_position": round(user_chart.neptune['position'], 3), "neptune_house": user_chart.neptune['house'], "neptune_retrograde": user_chart.neptune['retrograde']},
            10: {"pluto_sign": user_chart.pluto['sign'], "pluto_position": round(user_chart.pluto['position'], 3), "pluto_house": user_chart.pluto['house'], "pluto_retrograde": user_chart.pluto['retrograde']}
            }

        houses = {
            1: {"house_sign": user_chart.first_house['sign'], "house_position": round(user_chart.first_house['position'], 3)},
            2: {"house_sign": user_chart.second_house['sign'], "house_position": round(user_chart.second_house['position'], 3)},
            3: {"house_sign": user_chart.third_house['sign'], "house_position": round(user_chart.third_house['position'], 3)},
            4: {"house_sign": user_chart.fourth_house['sign'], "house_position": round(user_chart.fourth_house['position'], 3)},
            5: {"house_sign": user_chart.fifth_house['sign'], "house_position": round(user_chart.fifth_house['position'], 3)},
            6: {"house_sign": user_chart.sixth_house['sign'], "house_position": round(user_chart.sixth_house['position'], 3)},
            7: {"house_sign": user_chart.seventh_house['sign'], "house_position": round(user_chart.seventh_house['position'], 3)},
            8: {"house_sign": user_chart.eighth_house['sign'], "house_position": round(user_chart.eighth_house['position'], 3)},
            9: {"house_sign": user_chart.ninth_house['sign'], "house_position": round(user_chart.ninth_house['position'], 3)},
            10: {"house_sign": user_chart.tenth_house['sign'], "house_position": round(user_chart.tenth_house['position'], 3)},
            11: {"house_sign": user_chart.eleventh_house['sign'], "house_position": round(user_chart.eleventh_house['position'], 3)},
            12: {"house_sign": user_chart.twelfth_house['sign'], "house_position": round(user_chart.twelfth_house['position'], 3)}
            }

        result = {
            "planets": planets,
            "houses": houses
        }

        json_dump_results = json.dumps(result)

        return json_dump_results

    else:

        return jsonify({"Response": "Hello!"})


if __name__ == "__main__":
    
    app.run(host='0.0.0.0', debug=True)
