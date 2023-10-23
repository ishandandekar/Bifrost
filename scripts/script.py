# Contains the main graph which acts as a database
import pickle
from typing import Dict, List, Tuple, Union


class Graph:
    """
    Representing a **bidirectional Graph data structure**
    """

    def __init__(self) -> None:
        """
        Function called when object is instantiated,
        Sets up a list for vertices and a dictionary representing,
        adjacency list for each node
        """
        self.vertices: list = []
        self.vert_neigh_dict: Dict[str, List[Tuple[str, int]]] = {}

    def add_relation(self, start: str, end: str, time: int) -> None:
        """
        Adds a relation between two nodes

        Args:
            start (str): Node which represents the start of the direction
            end (str): Node which represents the end of the direction
            time (int): Time taken to reach `end` from `start` in minutes
        """
        if start not in self.vertices:
            self.vertices.append(start)
        if end not in self.vertices:
            self.vertices.append(end)
        if start not in self.vert_neigh_dict.keys():
            self.vert_neigh_dict[start] = []
        if end not in self.vert_neigh_dict.keys():
            self.vert_neigh_dict[end] = []

        if ((end, time) in self.vert_neigh_dict[start]) or (
            (start, time) in self.vert_neigh_dict[end]
        ):
            return
        self.vert_neigh_dict[start].append((end, time))
        self.vert_neigh_dict[end].append((start, time))

    @property
    def vertices_(self) -> list:
        """Returns a list of all the vertices in the network

        Returns:
            list: _description_
        """
        return self.vertices

    def get_neighbours(self, vertex: str) -> list:
        """Returns the neighbours of a vertex

        Args:
            vertex (str): Represents a vertex present in the network

        Raises:
            KeyError: Is raised when the `vertex` is not registered in the database

        Returns:
            list: Represents the neighbours of the `vertex`
        """
        if vertex in self.vertices:
            return [neighbour for neighbour, time in self.vert_neigh_dict[vertex]]
        else:
            raise KeyError(f"{vertex} not present as a vertex in data")

    def _get_adjacency_list(self, vertex: str) -> list:
        """Helper function which returns the adjacency list of the vertex

        Args:
            vertex (str): Represents a node in the network

        Raises:
            KeyError: Raised when `vertex` is not registered in database

        Returns:
            list: Represents the adjacency list of the `vertex`
        """
        if vertex in self.vertices:
            return self.vert_neigh_dict[vertex]
        else:
            raise KeyError(f"{vertex} not present as a vertex in database")

    def a_star_algorithm(
        self, start: str, end: str
    ) -> Union[Tuple[List[str], int], None]:
        """
        Performs A-star search algorithm to find the shortest path

        Args:
            start (str): Represents the start of the journey
            end (str): Represents the destination of the journey

        Returns:
            Union[Tuple[List[str], int], None]: Returns the path (as a list) and the time taken to traverse the path, or returns None, if no path is found
        """
        open_list = set([start])
        closed_list = set([])
        g = {}

        g[start] = 0
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] < g[n]:
                    n = v

            # if n == None:
            #     return None

            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(end)

                reconst_path.reverse()
                reconst_path[0] = start

                time_duration = 0
                for node in reconst_path:
                    if node == end:
                        break
                    for neighbour, time in self._get_adjacency_list(node):
                        if neighbour == reconst_path[reconst_path.index(node) + 1]:
                            time_duration += time
                return reconst_path, time_duration
            for m, weight in self._get_adjacency_list(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)

        return None


if __name__ == "__main__":
    graph = Graph()

    # Adding the Western Line
    graph.add_relation("Dahanu Road", "Vangaon", 13)
    graph.add_relation("Vangaon", "Boisar", 9)
    graph.add_relation("Boisar", "Umroli", 6)
    graph.add_relation("Umroli", "Palghar", 6)
    graph.add_relation("Palghar", "Kelve Rd.", 15)
    graph.add_relation("Kelve Rd.", "Saphale", 8)
    graph.add_relation("Saphale", "Vaitarna", 8)
    graph.add_relation("Vaitarna", "Virar", 9)
    graph.add_relation("Virar", "Nallasopara", 6)
    graph.add_relation("Nallasopara", "Vasai Rd.", 5)
    graph.add_relation("Vasai Rd.", "Naigaon", 5)
    graph.add_relation("Naigaon", "Bhayandar", 6)
    graph.add_relation("Bhayandar", "Mira Road", 5)
    graph.add_relation("Mira Road", "Dahisar", 5)
    graph.add_relation("Dahisar", "Borivali", 5)
    graph.add_relation("Borivali", "Kandivali", 6)
    graph.add_relation("Kandivali", "Malad", 3)
    graph.add_relation("Malad", "Goregaon", 5)
    graph.add_relation("Goregaon", "Ram Mandir", 2)
    graph.add_relation("Ram Mandir", "Jogeshwari", 3)
    graph.add_relation("Jogeshwari", "Andheri", 4)
    graph.add_relation("Andheri", "Vile Parle", 5)
    graph.add_relation("Vile Parle", "Santacruz", 3)
    graph.add_relation("Santacruz", "Khar Road", 2)
    graph.add_relation("Khar Road", "Bandra", 3)
    graph.add_relation("Bandra", "Mahim", 4)
    graph.add_relation("Mahim", "Matunga Rd.", 3)
    graph.add_relation("Matunga Rd.", "Dadar", 2)
    graph.add_relation("Dadar", "Prabhadevi", 2)
    graph.add_relation("Prabhadevi", "Lower Parel", 3)
    graph.add_relation("Lower Parel", "Mahalaxmi", 3)
    graph.add_relation("Mahalaxmi", "Mumbai Central (MMCT)", 3)
    graph.add_relation("Mumbai Central (MMCT)", "Grant Rd.", 2)
    graph.add_relation("Grant Rd.", "Charni Rd.", 3)
    graph.add_relation("Charni Rd.", "Marine Lines", 2)
    graph.add_relation("Marine Lines", "Churchgate", 3)

    # Adding the Central Line
    graph.add_relation("Chatrapati Shivaji Maharaj Terminus (CSMT)", "Masjid", 3)
    graph.add_relation("Masjid", "Sandhurst Rd.", 2)
    graph.add_relation("Sandhurst Rd.", "Byculla", 3)
    graph.add_relation("Byculla", "Chinchpokali", 2)
    graph.add_relation("Chinchpokali", "Currey Rd.", 2)
    graph.add_relation("Currey Rd.", "Parel", 3)
    graph.add_relation("Parel", "Dadar", 3)
    graph.add_relation("Dadar", "Matunga", 3)
    graph.add_relation("Matunga", "Sion", 4)
    graph.add_relation("Sion", "Kurla", 4)
    graph.add_relation("Kurla", "Vidya Vihar", 3)
    graph.add_relation("Vidya Vihar", "Ghatkopar", 3)
    graph.add_relation("Ghatkopar", "Vikhroli", 5)
    graph.add_relation("Vikhroli", "Kanjur Marg", 3)
    graph.add_relation("Kanjur Marg", "Bhandup", 3)
    graph.add_relation("Bhandup", "Nahur", 3)
    graph.add_relation("Nahur", "Mulund", 3)
    graph.add_relation("Mulund", "Thane", 4)
    graph.add_relation("Thane", "Kalwa", 4)
    graph.add_relation("Kalwa", "Mumbra", 6)
    graph.add_relation("Mumbra", "Diva", 4)
    graph.add_relation("Diva", "Kopar", 5)
    graph.add_relation("Kopar", "Dombivali", 4)
    graph.add_relation("Dombivali", "Thakurli", 3)
    graph.add_relation("Thakurli", "Kalyan", 6)
    graph.add_relation("Kalyan", "Shahad", 5)
    graph.add_relation("Shahad", "Ambivli", 3)
    graph.add_relation("Ambivli", "Titwala", 5)
    graph.add_relation("Titwala", "Khadavali", 6)
    graph.add_relation("Khadavali", "Vashind", 8)
    graph.add_relation("Vashind", "Asangaon", 6)
    graph.add_relation("Asangaon", "Atgaon", 9)
    graph.add_relation("Atgaon", "Thansit", 7)
    graph.add_relation("Thansit", "Khardi", 5)
    graph.add_relation("Khardi", "Umbernali", 6)
    graph.add_relation("Umbernali", "Kasara", 12)
    graph.add_relation("Kalyan", "Vitthalvadi", 5)
    graph.add_relation("Vitthalvadi", "Ulhasnagar", 3)
    graph.add_relation("Ulhasnagar", "Ambernath", 6)
    graph.add_relation("Ambernath", "Badlapur", 8)
    graph.add_relation("Badlapur", "Vangani", 9)
    graph.add_relation("Vangani", "Shelu", 4)
    graph.add_relation("Shelu", "Neral", 4)
    graph.add_relation("Neral", "Bhivpuri Rd.", 7)
    graph.add_relation("Bhivpuri Rd.", "Karjat", 9)
    graph.add_relation("Karjat", "Palasdhari", 5)
    graph.add_relation("Palasdhari", "Kelavali", 7)
    graph.add_relation("Kelavali", "Dolavali", 3)
    graph.add_relation("Dolavali", "Lowjee", 4)
    graph.add_relation("Lowjee", "Khopoli", 4)

    # Adding harbour line
    graph.add_relation("Chatrapati Shivaji Maharaj Terminus (CSMT)", "Masjid", 3)
    graph.add_relation("Masjid", "Sandhurst Rd.", 2)
    graph.add_relation("Sandhurst Rd.", "Dockyard Rd.", 2)
    graph.add_relation("Dockyard Rd.", "Reay Rd.", 2)
    graph.add_relation("Reay Rd.", "Cotton Green", 2)
    graph.add_relation("Cotton Green", "Sewri", 3)
    graph.add_relation("Sewri", "Vadala", 3)
    graph.add_relation("Vadala", "GTB Nagar", 4)
    graph.add_relation("GTB Nagar", "Chuna Bhatti", 3)
    graph.add_relation("Chuna Bhatti", "Kurla", 3)
    graph.add_relation("Kurla", "Tilak Nagar (LTT)", 3)
    graph.add_relation("Tilak Nagar (LTT)", "Chembur", 3)
    graph.add_relation("Chembur", "Govandi", 3)
    graph.add_relation("Govandi", "Mankhurd", 3)
    graph.add_relation("Mankhurd", "Vashi", 8)
    graph.add_relation("Vashi", "Sanpada", 3)
    graph.add_relation("Sanpada", "Juinagar", 3)
    graph.add_relation("Juinagar", "Nerul", 3)
    graph.add_relation("Nerul", "Seawood Darave", 3)
    graph.add_relation("Seawood Darave", "Belapur", 4)
    graph.add_relation("Belapur", "Kharghar", 4)
    graph.add_relation("Kharghar", "Manasarovar", 3)
    graph.add_relation("Manasarovar", "Khandeshwar", 3)
    graph.add_relation("Khandeshwar", "Panvel", 3)
    graph.add_relation("Vadala", "King's Circle", 4)
    graph.add_relation("King's Circle", "Mahim", 4)
    graph.add_relation("Mahim", "Bandra", 4)
    graph.add_relation("Bandra", "Khar Road", 3)
    graph.add_relation("Khar Road", "Santacruz", 2)
    graph.add_relation("Santacruz", "Vile Parle", 3)
    graph.add_relation("Vile Parle", "Andheri", 5)
    graph.add_relation("Andheri", "Jogeshwari", 4)
    graph.add_relation("Jogeshwari", "Ram Mandir", 3)
    graph.add_relation("Ram Mandir", "Goregaon", 2)

    # Adding metro line (Ghatkopar-Versova)
    graph.add_relation("Ghatkopar", "Jagruti Nagar", 3)
    graph.add_relation("Jagruti Nagar", "Asalpha", 2)
    graph.add_relation("Asalpha", "Saki Naka", 2)
    graph.add_relation("Saki Naka", "Marol Naka", 1)
    graph.add_relation("Marol Naka", "Airport Road", 2)
    graph.add_relation("Airport Road", "Chakala/JB Nagar", 2)
    graph.add_relation("Chakala/JB Nagar", "Western Express Highway", 2)
    graph.add_relation("Western Express Highway", "Andheri", 2)
    graph.add_relation("Andheri", "Azad Nagar", 4)
    graph.add_relation("Azad Nagar", "D N Nagar", 2)
    graph.add_relation("D N Nagar", "Versova", 1)

    # Adding Nerul-Uran line
    graph.add_relation("Nerul", "Seawood Darave", 3)
    graph.add_relation("Seawood Darave", "Bamadongri", 13)
    graph.add_relation("Belapur", "Bamadongri", 14)
    graph.add_relation("Bamadongri", "Kharkopar", 4)

    # Adding the Trans-Harbour line
    graph.add_relation("Thane", "Airoli", 8)
    graph.add_relation("Airoli", "Rabale", 3)
    graph.add_relation("Rabale", "Ghansoli", 3)
    graph.add_relation("Ghansoli", "Koparkhairane", 3)
    graph.add_relation("Koparkhairane", "Turbhe", 4)
    graph.add_relation("Turbhe", "Juinagar", 4)
    graph.add_relation("Juinagar", "Nerul", 4)
    graph.add_relation("Nerul", "Seawood Darave", 4)
    graph.add_relation("Seawood Darave", "Belapur", 5)
    graph.add_relation("Belapur", "Kharghar", 4)
    graph.add_relation("Kharghar", "Manasarovar", 3)
    graph.add_relation("Manasarovar", "Khandeshwar", 3)
    graph.add_relation("Khandeshwar", "Panvel", 5)
    graph.add_relation("Turbhe", "Sanpada", 4)
    graph.add_relation("Sanpada", "Vashi", 4)

    # Adding mono-rail
    graph.add_relation("Sant Gadge Maharaj Chowk", "Lower Parel", 2)
    graph.add_relation("Lower Parel", "Mint Colony", 2)
    graph.add_relation("Mint Colony", "Ambedkar Nagar", 3)
    graph.add_relation("Ambedkar Nagar", "Naigaon (near Dadar)", 3)
    graph.add_relation("Naigaon (near Dadar)", "Dadar East", 2)
    graph.add_relation("Dadar East", "Wadala Bridge", 3)
    graph.add_relation("Wadala Bridge", "Acharya Atre Nagar", 3)
    graph.add_relation("Acharya Atre Nagar", "Antop Hill", 2)
    graph.add_relation("Antop Hill", "GTB Nagar", 3)
    graph.add_relation("GTB Nagar", "Wadala", 2)
    graph.add_relation("Wadala", "Bhakti Park", 3)
    graph.add_relation("Bhakti Park", "Mysore Colony", 4)
    graph.add_relation("Mysore Colony", "Bharat Petroleum", 3)
    graph.add_relation("Bharat Petroleum", "Fertiliser Township", 3)
    graph.add_relation("Fertiliser Township", "VNP Marg Junction", 2)
    graph.add_relation("VNP Marg Junction", "Chembur", 3)

    # Adding 2A metro line
    graph.add_relation("D N Nagar", "Lower Oshiwara", 3)
    graph.add_relation("Lower Oshiwara", "Oshiwara", 3)
    graph.add_relation("Oshiwara", "Goregaon (West)", 3)
    graph.add_relation("Goregaon (West)", "Pahadi Goregaon", 2)
    graph.add_relation("Pahadi Goregaon", "Lower Malad", 2)
    graph.add_relation("Lower Malad", "Malad (West)", 2)
    graph.add_relation("Malad (West)", "Valnai", 3)
    graph.add_relation("Valnai", "Dahanukarwadi", 2)
    graph.add_relation("Dahanukarwadi", "Kandivali (West)", 2)
    graph.add_relation("Kandivali (West)", "Pahadi Eksar", 2)
    graph.add_relation("Pahadi Eksar", "Borivali (West)", 2)
    graph.add_relation("Borivali (West)", "Eksar", 2)
    graph.add_relation("Eksar", "Mandapeshwar", 3)
    graph.add_relation("Mandapeshwar", "Kandarpada", 2)
    graph.add_relation("Kandarpada", "Anand Nagar", 3)
    graph.add_relation("Anand Nagar", "Dahisar (East)", 2)
    graph.add_relation("Dahisar (East)", "Ovaripada", 3)
    graph.add_relation("Ovaripada", "Rashtriya Udyan", 2)
    graph.add_relation("Rashtriya Udyan", "Devipada", 3)
    graph.add_relation("Devipada", "Magathane", 2)
    graph.add_relation("Magathane", "Poisar", 2)
    graph.add_relation("Poisar", "Akurli", 2)
    graph.add_relation("Akurli", "Kurar", 3)
    graph.add_relation("Kurar", "Dindoshi", 2)
    graph.add_relation("Dindoshi", "Aarey", 3)
    graph.add_relation("Aarey", "Goregaon (East)", 4)
    graph.add_relation("Goregaon (East)", "Jogeshwari (East)", 2)
    graph.add_relation("Jogeshwari (East)", "Mogra", 2)
    graph.add_relation("Mogra", "Western Express Highway", 3)

    # Converting to pickle file to export graph network
    with open("network.pkl", "wb") as f:
        pickle.dump(graph, f)
    print("[INFO] Pickle file created. Network dump completed.")
