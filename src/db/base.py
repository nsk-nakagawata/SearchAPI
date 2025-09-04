from abc import ABC, abstractmethod

class VectorDBBase(ABC):
    @abstractmethod
    def add_vector(self, vector, metadata):
        pass

    @abstractmethod
    def update_vector(self, vector_id, vector, metadata):
        pass

    @abstractmethod
    def delete_vector(self, vector_id):
        pass

    @abstractmethod
    def search_vectors(self, query_vector, top_k=10):
        pass