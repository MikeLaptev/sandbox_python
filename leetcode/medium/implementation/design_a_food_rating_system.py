import heapq
from collections import defaultdict
from typing import List, Dict


class DesignFoodRatingSystem:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_2_cuisines: Dict[str, str] = {
            foods[i]: cuisines[i] for i in range(len(foods))
        }
        self.food_2_ratings: Dict[str, int] = {
            foods[i]: ratings[i] for i in range(len(foods))
        }
        self.cuisines_2_rating_2_foods: Dict[str, Dict[int, List]] = {
            cuisines[i]: {} for i in range(len(cuisines))
        }
        for i, cuisine in enumerate(cuisines):
            if ratings[i] not in self.cuisines_2_rating_2_foods[cuisine]:
                self.cuisines_2_rating_2_foods[cuisine][ratings[i]] = []
            self.cuisines_2_rating_2_foods[cuisine][ratings[i]].append(foods[i])

    def change_rating(self, food: str, new_rating: int) -> None:
        old_rating = self.food_2_ratings[food]
        self.food_2_ratings[food] = new_rating
        self.cuisines_2_rating_2_foods[self.food_2_cuisines[food]][old_rating].remove(
            food
        )
        if not self.cuisines_2_rating_2_foods[self.food_2_cuisines[food]][old_rating]:
            del self.cuisines_2_rating_2_foods[self.food_2_cuisines[food]][old_rating]
        if new_rating not in self.cuisines_2_rating_2_foods[self.food_2_cuisines[food]]:
            self.cuisines_2_rating_2_foods[self.food_2_cuisines[food]][new_rating] = []
        self.cuisines_2_rating_2_foods[self.food_2_cuisines[food]][new_rating].append(
            food
        )

    def highest_rated(self, cuisine: str) -> str:
        stats: Dict[int, List[str]] = self.cuisines_2_rating_2_foods[cuisine]
        rating = max(stats.keys())
        food = sorted(self.cuisines_2_rating_2_foods[cuisine][rating])[0]
        return food


class DesignFoodRatingSystemOpt:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.rated_cuisine = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = (rating, cuisine)
            self.rated_cuisine[cuisine].append((-rating, food))

        for cuisine in self.rated_cuisine:
            heapq.heapify(self.rated_cuisine[cuisine])

    def change_rating(self, food: str, newRating: int) -> None:
        _, curr_cuisine = self.foods[food]
        self.foods[food] = (newRating, curr_cuisine)
        heapq.heappush(self.rated_cuisine[curr_cuisine], (-newRating, food))

    def highest_rated(self, cuisine: str) -> str:
        while (
            self.rated_cuisine[cuisine][0][0]
            != -self.foods[self.rated_cuisine[cuisine][0][1]][0]
        ):
            heapq.heappop(self.rated_cuisine[cuisine])
        return self.rated_cuisine[cuisine][0][1]


if __name__ == "__main__":
    # acceptance 1.1
    sut: DesignFoodRatingSystem = DesignFoodRatingSystem(
        foods=["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        cuisines=["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        ratings=[9, 12, 8, 15, 14, 7],
    )

    assert "kimchi" == sut.highest_rated("korean")
    assert "ramen" == sut.highest_rated("japanese")

    sut.change_rating("sushi", 16)
    assert "sushi" == sut.highest_rated("japanese")

    sut.change_rating("ramen", 16)
    assert "ramen" == sut.highest_rated("japanese")

    # acceptance 1.2
    sut: DesignFoodRatingSystem = DesignFoodRatingSystem(
        foods=["emgqdbo", "jmvfxjohq", "qnvseohnoe", "yhptazyko", "ocqmvmwjq"],
        cuisines=["snaxol", "snaxol", "snaxol", "fajbervsj", "fajbervsj"],
        ratings=[2, 6, 18, 6, 5],
    )
    sut.change_rating("qnvseohnoe", 11)
    sut.highest_rated("fajbervsj")
    sut.change_rating("emgqdbo", 3)
    sut.change_rating("jmvfxjohq", 9)
    sut.change_rating("emgqdbo", 14)
    sut.highest_rated("fajbervsj")
    sut.highest_rated("snaxol")

    # acceptance 2.1
    sut: DesignFoodRatingSystemOpt = DesignFoodRatingSystemOpt(
        foods=["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        cuisines=["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        ratings=[9, 12, 8, 15, 14, 7],
    )

    assert "kimchi" == sut.highest_rated("korean")
    assert "ramen" == sut.highest_rated("japanese")

    sut.change_rating("sushi", 16)
    assert "sushi" == sut.highest_rated("japanese")

    sut.change_rating("ramen", 16)
    assert "ramen" == sut.highest_rated("japanese")

    # acceptance 2.2
    sut: DesignFoodRatingSystemOpt = DesignFoodRatingSystemOpt(
        foods=["emgqdbo", "jmvfxjohq", "qnvseohnoe", "yhptazyko", "ocqmvmwjq"],
        cuisines=["snaxol", "snaxol", "snaxol", "fajbervsj", "fajbervsj"],
        ratings=[2, 6, 18, 6, 5],
    )
    sut.change_rating("qnvseohnoe", 11)
    sut.highest_rated("fajbervsj")
    sut.change_rating("emgqdbo", 3)
    sut.change_rating("jmvfxjohq", 9)
    sut.change_rating("emgqdbo", 14)
    sut.highest_rated("fajbervsj")
    sut.highest_rated("snaxol")
