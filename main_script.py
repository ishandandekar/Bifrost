# Contains the main graph which acts as a database
from typing import Dict, List, Tuple


class Graph:
    def __init__(self) -> None:
        self.vertices: list = []
        self.vert_neigh_dict: Dict[str, List[Tuple[str, int]]] = {}

    def add_relation(self, start: str, end: str, time: int) -> None:
        if start not in self.vertices:
            self.vertices.append(start)
        if end not in self.vertices:
            self.vertices.append(end)
        if self.vert_neigh_dict[start] == None:
            self.vert_neigh_dict[start] = []
        if self.vert_neigh_dict[end] == None:
            self.vert_neigh_dict[end] = []

        if ((end, time) in self.vert_neigh_dict[start]) or ((start, time) in self.vert_neigh_dict[end]):
            return
        self.vert_neigh_dict[start].append((end, time))
        self.vert_neigh_dict[end].append((start, time))

    @property
    def vertices_(self) -> list:
        return self.vertices

    def get_neighbours(self, vertex: str) -> list:
        if vertex in self.vertices:
            return [neighbour for neighbour, time in self.vert_neigh_dict[vertex]]
        else:
            raise KeyError(f'{vertex} not present as a vertex in database')


if __name__ == '__main__':
    graph = Graph()

    # Adding the Western Line
    graph.add_relation('Dahanu Rd.', 'Vangaon', 13)
    graph.add_relation('Vangaon', 'Boisar', 9)
    graph.add_relation('Boisar', 'Umroli', 6)
    graph.add_relation('Umroli', 'Palghar', 6)
    graph.add_relation('Palghar', 'Kelve Rd.', 15)
    graph.add_relation('Kelve Rd.', 'Saphale', 8)
    graph.add_relation('Saphale', 'Vaitarna', 8)
    graph.add_relation('Vaitarna', 'Virar', 9)
    graph.add_relation('Virar', 'Nallasopara', 6)
    graph.add_relation('Nallasopara', 'Vasai Rd.', 5)
    graph.add_relation('Vasai Rd.', 'Naigaon', 5)
    graph.add_relation('Naigaon', 'Bhayandar', 6)
    graph.add_relation('Bhayandar', 'Mira Road', 5)
    graph.add_relation('Mira Road', 'Dahisar', 5)
    graph.add_relation('Dahisar', 'Borivali', 5)
    graph.add_relation('Borivali', 'Kandivali', 6)
    graph.add_relation('Kandivali', 'Malad', 3)
    graph.add_relation('Malad', 'Goregaon', 5)
    graph.add_relation('Goregaon', 'Ram Mandir', 2)
    graph.add_relation('Ram Mandir', 'Jogeshwari', 3)
    graph.add_relation('Jogeshwari', 'Andheri', 4)
    graph.add_relation('Andheri', 'Vile Parle', 5)
    graph.add_relation('Vile Parle', 'Santacruz', 3)
    graph.add_relation('Santacruz', 'Khar Road', 2)
    graph.add_relation('Khar Road', 'Bandra', 3)
    graph.add_relation('Bandra', 'Mahim', 4)
    graph.add_relation('Mahim', 'Matunga Rd.', 3)
    graph.add_relation('Matunga Rd.', 'Dadar', 2)
    graph.add_relation('Dadar', 'Prabhadevi', 2)
    graph.add_relation('Prabhadevi', 'Lower Parel', 3)
    graph.add_relation('Lower Parel', 'Mahalaxmi', 3)
    graph.add_relation('Mahalaxmi', 'Mumbai Central (MMCT)', 3)
    graph.add_relation('Mumbai Central (MMCT)', 'Grant Rd.', 2)
    graph.add_relation('Grant Rd.', 'Charni Rd.', 3)
    graph.add_relation('Charni Rd.', 'Marine Lines', 2)
    graph.add_relation('Marine Lines', 'Churchgate', 3)

    # Adding the Central Line
    graph.add_relation(
        'Chatrapati Shivaji Maharaj Terminus (CSMT)', 'Masjid', 3)
    graph.add_relation('Masjid', 'Sandhurst Rd.', 2)
    graph.add_relation('Sandhurst Rd.', 'Byculla', 3)
    graph.add_relation('Byculla', 'Chinchpokali', 2)
    graph.add_relation('Chinchpokali', 'Currey Rd.', 2)
    graph.add_relation('Currey Rd.', 'Parel', 3)
    graph.add_relation('Parel', 'Dadar', 3)
    graph.add_relation('Dadar', 'Matunga', 3)
    graph.add_relation('Matunga', 'Sion', 4)
    graph.add_relation('Sion', 'Kurla', 4)
    graph.add_relation('Kurla', 'Vidya Vihar', 3)
    graph.add_relation('Vidya Vihar', 'Ghatkopar', 3)
    graph.add_relation('Ghatkopar', 'Vikhroli', 5)
    graph.add_relation('Vikhroli', 'Kanjur Marg', 3)
    graph.add_relation('Kanjur Marg', 'Bhandup', 3)
    graph.add_relation('Bhandup', 'Nahur', 3)
    graph.add_relation('Nahur', 'Mulund', 3)
    graph.add_relation('Mulund', 'Thane', 4)
    graph.add_relation('Thane', 'Kalwa', 4)
    graph.add_relation('Kalwa', 'Mumbra', 6)
    graph.add_relation('Mumbra', 'Diva', 4)
    graph.add_relation('Diva', 'Kopar', 5)
    graph.add_relation('Kopar', 'Dombivali', 4)
    graph.add_relation('Dombivali', 'Thakurli', 3)
    graph.add_relation('Thakurli', 'Kalyan', 6)
    graph.add_relation('Kalyan', 'Shahad', 5)
    graph.add_relation('Shahad', 'Ambivli', 3)
    graph.add_relation('Ambivli', 'Titwala', 5)
    graph.add_relation('Titwala', 'Khadavali', 6)
    graph.add_relation('Khadavali', 'Vashind', 8)
    graph.add_relation('Vashind', 'Asangaon', 6)
    graph.add_relation('Asangaon', 'Atgaon', 9)
    graph.add_relation('Atgaon', 'Thansit', 7)
    graph.add_relation('Thansit', 'Khardi', 5)
    graph.add_relation('Khardi', 'Umbernali', 6)
    graph.add_relation('Umbernali', 'Kasara', 12)
    graph.add_relation('Kalyan', 'Vitthalvadi', 5)
    graph.add_relation('Vitthalvadi', 'Ulhasnagar', 3)
    graph.add_relation('Ulhasnagar', 'Ambernath', 6)
    graph.add_relation('Ambernath', 'Badlapur', 8)
    graph.add_relation('Badlapur', 'Vangani', 9)
    graph.add_relation('Vangani', 'Shelu', 4)
    graph.add_relation('Shelu', 'Neral', 4)
    graph.add_relation('Neral', 'Bhivpuri Rd.', 7)
    graph.add_relation('Bhivpuri Rd.', 'Karjat', 9)
    graph.add_relation('Karjat', 'Palasdhari', 5)
    graph.add_relation('Palasdhari', 'Kelavali', 7)
    graph.add_relation('Kelavali', 'Dolavali', 3)
    graph.add_relation('Dolavali', 'Lowjee', 4)
    graph.add_relation('Lowjee', 'Khopoli', 4)

    # Adding harbour line
    graph.add_relation(
        'Chatrapati Shivaji Maharaj Terminus (CSMT)', 'Masjid', 3)
    graph.add_relation('Masjid', 'Sandhurst Rd.', 2)
    graph.add_relation('Sandhurst Rd.', 'Dockyard Rd.', 2)
    graph.add_relation('Dockyard Rd.', 'Reay Rd.', 2)
    graph.add_relation('Reay Rd.', 'Cotton Green', 2)
    graph.add_relation('Cotton Green', 'Sewri', 3)
    graph.add_relation('Sewri', 'Vadala', 3)
    graph.add_relation('Vadala', 'GTB Nagar', 4)
    graph.add_relation('GTB Nagar', 'Chuna Bhatti', 3)
    graph.add_relation('Chuna Bhatti', 'Kurla', 3)
    graph.add_relation('Kurla', 'Tilak Nagar (LTT)', 3)
    graph.add_relation('Tilak Nagar (LTT)', 'Chembur', 3)
    graph.add_relation('Chembur', 'Govandi', 3)
    graph.add_relation('Govandi', 'Mankhurd', 3)
    graph.add_relation('Mankhurd', 'Vashi', 8)
    graph.add_relation('Vashi', 'Sanpada', 3)
    graph.add_relation('Sanpada', 'Juinagar', 3)
    graph.add_relation('Juinagar', 'Nerul', 3)
    graph.add_relation('Nerul', 'Seawood Darave', 3)
    graph.add_relation('Seawood Darave', 'Belapur', 4)
