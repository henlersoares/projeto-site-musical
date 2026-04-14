import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [albums, setAlbums] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Buscar álbuns da API Django
    fetch('http://localhost:8000/api/albums/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro na requisição');
        }
        return response.json();
      })
      .then(data => {
        setAlbums(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Carregando álbuns...</div>;
  if (error) return <div>Erro: {error}</div>;

  return (
    <div className="App">
      <h1> Site Musical</h1>
      <h2>Álbuns disponíveis:</h2>
      {albums.length === 0 ? (
        <p>Nenhum álbum cadastrado ainda.</p>
      ) : (
        <ul>
          {albums.map(album => (
            <li key={album.id}>
              <strong>{album.title}</strong> - {album.artist}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;