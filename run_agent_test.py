# # test_root_pipeline.py
# from root_agent.agent import root_agent

# def test_root_agent_pipeline():
#     test_queries = [
#         "Explain how Vision Transformer works.",
#         "What is the weather today?", 
#         "How does inflation affect currency value?",
#         "Tell me about machine learning concepts in the PDF.",
#         "What's the capital of France?"
#     ]
    
#     print("🚀 Testing Root Agent Pipeline")
#     print("="*60)
    
#     for i, query in enumerate(test_queries, 1):
#         print(f"\n[Test {i}] Query: {query}")
#         print("-" * 50)
        
#         try:
#             # Invoke the root agent
#             response = root_agent.run_async(query)
#             print(f"Response: {response}")
            
#         except Exception as e:
#             print(f"Error: {e}")
    
#     print("\n✅ Pipeline testing completed!")

# if __name__ == "__main__":
#     test_root_agent_pipeline()

# test_async_generator.py
# import asyncio
# from root_agent.agent import root_agent

# async def test_root_agent_async_generator():
#     test_queries = [
#         "Explain how Vision Transformer works.",
#         "What is the weather today?", 
#         "How does inflation affect currency value?",
#         "Tell me about machine learning concepts in the PDF.",
#         "What's the capital of France?"
#     ]
    
#     print("🚀 Testing Root Agent Pipeline with Async Generator")
#     print("="*60)
    
#     for i, query in enumerate(test_queries, 1):
#         print(f"\n[Test {i}] Query: {query}")
#         print("-" * 50)
        
#         try:
#             # Get the async generator
#             async_gen = root_agent.run_async(query)
            
#             # Collect all chunks from the generator
#             response_chunks = []
#             async for chunk in async_gen:
#                 response_chunks.append(chunk)
#                 print(f"📦 Chunk: {chunk}")  # Optional: see individual chunks
            
#             # Combine all chunks for final response
#             full_response = ''.join(str(chunk) for chunk in response_chunks)
#             print(f"🎯 Full Response: {full_response}")
            
#         except Exception as e:
#             print(f"❌ Error: {e}")
#             import traceback
#             traceback.print_exc()

# if __name__ == "__main__":
#     asyncio.run(test_root_agent_async_generator())

###❌ Error: 'str' object has no attribute 'model_copy'
# Traceback (most recent call last):
#   File "e:\Python Stuff\WF\run_agent_test.py", line 59, in test_root_agent_async_generator
#     async for chunk in async_gen:
#   File "E:\Python Stuff\GenAI\Lib\site-packages\google\adk\agents\base_agent.py", line 140, in run_async
#     ctx = self._create_invocation_context(parent_context)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "E:\Python Stuff\GenAI\Lib\site-packages\google\adk\agents\base_agent.py", line 248, in _create_invocation_context
#     invocation_context = parent_context.model_copy(update={'agent': self})
#                          ^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'str' object has no attribute 'model_copy'
# robust_async_test.py
# test_input_formats.py
# check_message_classes.py
import asyncio
from root_agent.agent import root_agent

def check_google_adk_imports():
    print("🔍 Checking Google ADK imports and message classes")
    print("="*60)
    
    try:
        # Try to import common Google ADK message classes
        from google.adk.agents import Message
        print("✅ Found google.adk.agents.Message")
        return Message
    except ImportError:
        print("❌ google.adk.agents.Message not found")
    
    try:
        from google.adk.sessions import Message
        print("✅ Found google.adk.core.Message")
        return Message
    except ImportError:
        print("❌ google.adk.core.Message not found")
    
    try:
        from google.adk import Message
        print("✅ Found google.adk.Message")
        return Message
    except ImportError:
        print("❌ google.adk.Message not found")
    
    # Check what's available in the agent module
    try:
        import google.adk.agents as adk_agents
        print(f"\n📦 Available in google.adk.agents:")
        for attr in dir(adk_agents):
            if not attr.startswith('_'):
                print(f"  - {attr}")
        
        # Look for message-related classes
        message_classes = [attr for attr in dir(adk_agents) if 'message' in attr.lower()]
        if message_classes:
            print(f"\n💬 Message-related classes:")
            for cls in message_classes:
                print(f"  - {cls}")
                
    except Exception as e:
        print(f"❌ Error checking google.adk.agents: {e}")
    
    return None

async def test_with_message_class():
    Message = check_google_adk_imports()
    
    if Message:
        print(f"\n🧪 Testing with Message class")
        print("-" * 40)
        
        query_text = "Explain how Vision Transformer works."
        
        try:
            # Create proper message object
            message = Message(content=query_text, role="user")
            print(f"📨 Created message: {message}")
            
            async_gen = root_agent.run_async(message)
            response = []
            async for chunk in async_gen:
                response.append(str(chunk))
            
            full_response = ''.join(response)
            print(f"✅ Success: {full_response}")
            
        except Exception as e:
            print(f"❌ Failed with Message class: {e}")
            
            # Try different Message constructor patterns
            try:
                message = Message(query_text)
                async_gen = root_agent.run_async(message)
                response = []
                async for chunk in async_gen:
                    response.append(str(chunk))
                print(f"✅ Success with simple Message: {''.join(response)}")
            except Exception as e2:
                print(f"❌ Also failed with simple Message: {e2}")

if __name__ == "__main__":
    asyncio.run(test_with_message_class())