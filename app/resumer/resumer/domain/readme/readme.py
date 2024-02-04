from pydantic import BaseModel, FilePath


class Readme(BaseModel):
    profile_file_path: FilePath = FilePath("resumer/data/profile")
    blog_articles_file_path: FilePath = FilePath("resumer/data/blog_article")
