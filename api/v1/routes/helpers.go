package helpers

import (
	"context"
	"fmt"
	"log"
	"os"
	"path/filepath"

	"github.com/go-redis/redis/v9"
)

// GetRedisClient returns a redis client instance
func GetRedisClient() (*redis.Client, error) {
	redisAddr := os.Getenv("REDIS_ADDR")
	if redisAddr == "" {
		return nil, fmt.Errorf("REDIS_ADDR environment variable is not set")
	}

	client := redis.NewClient(&redis.Options{
		Addr:     redisAddr,
		DB:       0, // use default DB
		PoolSize: 10,
	})

	_, err := client.Ping(context.Background()).Result()
	if err!= nil {
		return nil, err
	}

	return client, nil
}

// GetCachePath returns the path to the cache directory
func GetCachePath() string {
	cacheDir := os.Getenv("CACHE_DIR")
	if cacheDir == "" {
		cacheDir = filepath.Join(os.Getenv("HOME"), ".cache", "cache-redis-config")
	}

	if err := os.MkdirAll(cacheDir, os.ModePerm); err!= nil {
		log.Fatal(err)
	}

	return cacheDir
}