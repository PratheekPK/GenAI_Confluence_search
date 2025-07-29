import build_vectorstore
import scrape_confluence

if __name__ == "__main__":
    scrape_confluence.scrape_main()
    print("Finished part 1")
    build_vectorstore.build_index()