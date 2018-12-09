var staticCacheName = 'ascensor-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/static/ascensor/css/cuerpo.css',
        '/static/ascensor/css/base.css',
        '/static/ascensor/css/login.css',
        '/static/ascensor/img/facebook.png',
        '/static/ascensor/img/Fondo2.jpg',
        '/static/ascensor/img/Logo.png',
        '/static/ascensor/img/LogoElevator.png',
        '/static/ascensor/img/user.png',
        '/ascensor/ListadoClientes.html',
        '/ascensor/ListadoOrdenes.html',
        '/ascensor/ListadoTecnicos.html',
        '/ascensor/MisClientes.html',
        '/ascensor/MisOrdenes.html',
        '/ascensor/NuevaOrden.html'
      ]);
    })
  );
});

// Si hay red, lee de la red y guarda en cache la última versión, si no hay red, lee del cache.
self.addEventListener('fetch', (event) => {
  event.respondWith(async function() {
    const cache = await caches.open(staticCacheName);
    try {
      const networkResponse = await fetch(event.request);
      event.waitUntil(
        cache.put(event.request, networkResponse.clone())
      );
      return networkResponse;
    }
    catch (err) {
      const cachedResponse = await cache.match(event.request);
      if (cachedResponse) return cachedResponse;
    }
  }());
});