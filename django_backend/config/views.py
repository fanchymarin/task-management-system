from django.http import JsonResponse
from django.db import connections
from django_redis import get_redis_connection

def health_check(request):
	# Check database connections
	db_ok = all(conn.cursor().execute("SELECT 1") for conn in connections.all())

	# Check cache connection
	try:
		cache = get_redis_connection("default")
		cache.ping()
		cache_ok = True
	except Exception:
		cache_ok = False

	status_code = 200 if db_ok and cache_ok else 503
	return JsonResponse({"status": "ok" if db_ok and cache_ok else "unhealthy"}, status=status_code)